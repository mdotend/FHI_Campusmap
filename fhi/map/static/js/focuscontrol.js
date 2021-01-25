function changeActiveTab(pTab){
    var active_tabs = document.getElementsByClassName("tab_focused");
    for (var i = 0; i<active_tabs.length;i++){
      active_tabs[i].classList.replace("tab_focused","tab_background");
    }
    document.getElementById(pTab).classList.replace("tab_background","tab_focused");
}

function setActiveCard(pCards){
  var active_cards = document.getElementsByClassName("card-focused");
  for (var i = 0; i<active_cards.length;i++){
    active_tabs[i].classList.remove("card-focused");
  }
  if (pCards != ""){
    pCards.split(",").forEach(function(card){
      document.getElementById(card + "-card").classList.add("card-focused");
    });
  }

  
}