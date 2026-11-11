// version: 7.12.0.a.1.7.0
// sha: 8469fc403f7785dde88b8a8b800568ea0e850bb0
function SetBookmark(){var o=window.parent,t=window.location.href;o.SetBookmark(t.substring(t.toLowerCase().lastIndexOf("/scormcontent/")+14,t.length),document.title),o.CommitData()}SetBookmark();