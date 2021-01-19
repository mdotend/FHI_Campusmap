function changeActiveTab(pTab){
    var active_tabs = document.getElementsByClassName("tab_focused");
    for (var i = 0; i<active_tabs.length;i++){
      active_tabs[i].classList.replace("tab_focused","tab_background");
    }
    document.getElementById(pTab).classList.replace("tab_background","tab_focused");
}