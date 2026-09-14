// version: 7.12.0.a.1.6.4
// sha: 2b5fc1a917420ce3ab1b0de2ee8487bec08b6a4d
function SetBookmark(){var o=window.parent,t=window.location.href;o.SetBookmark(t.substring(t.toLowerCase().lastIndexOf("/scormcontent/")+14,t.length),document.title),o.CommitData()}SetBookmark();