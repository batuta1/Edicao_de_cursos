// version: 7.12.0.a.1.7.2
// sha: f67035d5ef0642e33b393d715fd84025d0b87b57
function SetBookmark(){var o=window.parent,t=window.location.href;o.SetBookmark(t.substring(t.toLowerCase().lastIndexOf("/scormcontent/")+14,t.length),document.title),o.CommitData()}SetBookmark();