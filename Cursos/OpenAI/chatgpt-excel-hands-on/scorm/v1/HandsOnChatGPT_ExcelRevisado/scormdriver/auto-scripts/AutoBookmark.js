// version: 7.12.0.a.1.6.5
// sha: 411a8ff6993b8387b306ea5eb02fb94e6603e507
function SetBookmark(){var o=window.parent,t=window.location.href;o.SetBookmark(t.substring(t.toLowerCase().lastIndexOf("/scormcontent/")+14,t.length),document.title),o.CommitData()}SetBookmark();