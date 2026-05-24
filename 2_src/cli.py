#!/usr/bin/env python3
"""Command-line interface for SCORM course processing."""

import argparse
import sys
from pathlib import Path

from config.paths import ScormPaths
from config.settings import settings
from scorm.deserializer import CourseDeserializer
from scorm.extractor import LessonExtractor
from scorm.serializer import CourseSerializer
from scorm.analyzer import ContentTypeAnalyzer, CourseMapGenerator
from utils.validators import LessonValidator


def cmd_deserialize(args):
    """Deserialize base64 SCORM data to JSON."""
    paths = ScormPaths()

    if args.input_file:
        # Deserialize from file
        input_path = Path(args.input_file)
        if not input_path.exists():
            print(f"Error: Input file not found: {input_path}")
            return 1

        course_data = CourseDeserializer.deserialize_from_file(input_path)
        output_path = paths.get_course_json_path(args.course)
        CourseDeserializer.save_to_json_file(course_data, output_path)
        print(f"Deserialized course saved to: {output_path}")

    elif args.base64_string:
        # Deserialize from command-line string
        course_data = CourseDeserializer.deserialize_from_string(args.base64_string)
        output_path = paths.get_course_json_path(args.course)
        CourseDeserializer.save_to_json_file(course_data, output_path)
        print(f"Deserialized course saved to: {output_path}")

    else:
        print("Error: Provide either --input-file or --base64-string")
        return 1

    return 0


def cmd_extract(args):
    """Extract lessons from course JSON."""
    paths = ScormPaths()
    extractor = LessonExtractor(paths)

    course_path = paths.get_course_json_path(args.course)
    if not course_path.exists():
        print(f"Error: Course JSON not found: {course_path}")
        print(f"Run 'deserialize' first to create it.")
        return 1

    lessons_dir = extractor.extract_and_save(course_path, args.course)
    print(f"Lessons extracted to: {lessons_dir}")
    return 0


def cmd_serialize(args):
    """Reconstruct course from edited lessons."""
    paths = ScormPaths()
    serializer = CourseSerializer(paths)

    original_path = paths.get_course_json_path(args.course)
    if not original_path.exists():
        print(f"Error: Course JSON not found: {original_path}")
        return 1

    # Optional HTML source for automatic update
    html_source = None
    if args.html_source:
        html_source = Path(args.html_source)
        if not html_source.exists():
            print(f"Warning: HTML file not found: {html_source}")
            html_source = None

    outputs = serializer.full_serialize_and_export(
        original_path,
        args.course,
        html_source
    )

    print("Serialization complete. Output files:")
    for key, path in outputs.items():
        print(f"  {key}: {path}")

    return 0


def cmd_analyze(args):
    """Analyze course structure and content types."""
    paths = ScormPaths()

    course_path = paths.get_course_json_path(args.course)
    if not course_path.exists():
        print(f"Error: Course JSON not found: {course_path}")
        return 1

    from utils.file_utils import read_json

    course_data = read_json(course_path)

    if args.type_count:
        # Count content types
        analyzer = ContentTypeAnalyzer()
        distribution = analyzer.analyze_course(course_data)
        print("\nContent type distribution:")
        for type_name, count in sorted(distribution.items(), key=lambda x: -x[1]):
            print(f"  {type_name}: {count}")

        # Save to file if requested
        if args.output:
            output_path = Path(args.output)
            analyzer.save_analysis(distribution, output_path)
            print(f"Analysis saved to: {output_path}")

    if args.detailed_map:
        # Generate detailed map
        generator = CourseMapGenerator()
        output_path = Path(args.output) if args.output else paths.get_course_map_path(args.course)
        generator.save_course_map(course_data, output_path)
        print(f"Detailed course map saved to: {output_path}")

    return 0


def cmd_search(args):
    """Search for text in lesson files."""
    paths = ScormPaths()
    validator = LessonValidator()

    lessons_dir = paths.get_lessons_dir(args.course)
    if not lessons_dir.exists():
        print(f"Error: Lessons directory not found: {lessons_dir}")
        return 1

    results = validator.find_text_in_lessons(lessons_dir, args.text)

    print(f"\nSearching for: '{args.text}'")
    print("-" * 80)

    found_count = 0
    for filename, result in results.items():
        if result["found_anywhere"]:
            found_count += 1
            location = "in lesson content" if result["found_in_lesson"] else "in metadata"
            print(f"✓ {filename} ({location})")

    if found_count == 0:
        print("Text not found in any lessons.")
    else:
        print(f"\nFound in {found_count} file(s)")

    return 0


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="SCORM course processing pipeline"
    )
    parser.add_argument("--version", action="version", version="0.1.0")

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Deserialize command
    parser_deser = subparsers.add_parser(
        "deserialize",
        help="Convert base64 SCORM data to JSON"
    )
    parser_deser.add_argument("--course", required=True, help="Course name")
    parser_deser.add_argument(
        "--input-file",
        help="Base64 file to deserialize"
    )
    parser_deser.add_argument(
        "--base64-string",
        help="Base64 string to deserialize"
    )
    parser_deser.set_defaults(func=cmd_deserialize)

    # Extract command
    parser_extract = subparsers.add_parser(
        "extract",
        help="Extract lessons from course"
    )
    parser_extract.add_argument("--course", required=True, help="Course name")
    parser_extract.set_defaults(func=cmd_extract)

    # Serialize command
    parser_serial = subparsers.add_parser(
        "serialize",
        help="Reconstruct course from edited lessons"
    )
    parser_serial.add_argument("--course", required=True, help="Course name")
    parser_serial.add_argument(
        "--html-source",
        help="Source HTML file to update with new base64"
    )
    parser_serial.set_defaults(func=cmd_serialize)

    # Analyze command
    parser_analyze = subparsers.add_parser(
        "analyze",
        help="Analyze course structure"
    )
    parser_analyze.add_argument("--course", required=True, help="Course name")
    parser_analyze.add_argument(
        "--type-count",
        action="store_true",
        help="Count content types"
    )
    parser_analyze.add_argument(
        "--detailed-map",
        action="store_true",
        help="Generate detailed course map"
    )
    parser_analyze.add_argument(
        "--output",
        help="Output file path"
    )
    parser_analyze.set_defaults(func=cmd_analyze)

    # Search command
    parser_search = subparsers.add_parser(
        "search",
        help="Search for text in lessons"
    )
    parser_search.add_argument("--course", required=True, help="Course name")
    parser_search.add_argument("--text", required=True, help="Text to search for")
    parser_search.set_defaults(func=cmd_search)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
