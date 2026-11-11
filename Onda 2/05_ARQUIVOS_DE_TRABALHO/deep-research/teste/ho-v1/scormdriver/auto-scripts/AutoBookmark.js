// version: 7.12.0.a.1.7.1
// sha: 8953211661544016c9a06b40d9efa0a03cd1f426
function SetBookmark(){var o=window.parent,t=window.location.href;o.SetBookmark(t.substring(t.toLowerCase().lastIndexOf("/scormcontent/")+14,t.length),document.title),o.CommitData()}SetBookmark();