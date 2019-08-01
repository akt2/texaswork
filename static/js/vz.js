// The following code was modified from https://community.tableau.com/thread/135473.

// var vizDiv=document.getElementById('viz');
// var vizURL= "https://public.tableau.com/views/Project3Rev2/Top10MedianHourlyWagebyRegion?:embed=y&:display_count=yes&publish=yes&:origin=viz_share_link";
// var options= {
//     width:'1400px',
//     height: '1000px',
//     hideToolbar: true,
//     hideTabs: false,
//     onFirstInteractive: function(){
//         document.getElementById('sheetName') .innerHTML=viz.getWorkbook().getActiveSheet().getName();
//     }
// };
// viz= new tableauSoftware.Viz(divElement, vizURL, options);
// viz.addEventListener('tabswitch',function(event){
//     document.getElementById('sheetName') .innerHTML=event.getNewSheetName();
// });
// function switchView(sheetName){
//     workbook=viz.getWorkbook();
//     workbook.activateSheetAsync(sheetName);
// }

var divElement = document.getElementById('viz1564249110186');
var vizElement = divElement.getElementsByTagName('object')[0];
vizElement.style.width='100%';
vizElement.style.height=newFunction();
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);

function newFunction() {
    return (divElement.offsetWidth * 0.75) + 'px';
}

window.onscroll = function() {myFunction()};
    
    var header = document.getElementById("navy");
    var sticky = header.offsetTop;
    
    function myFunction() {
      if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
    }

    // tableau.html
    var divElement = document.getElementById('viz1564624310615');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);

    // models.html
  var divElement = document.getElementById('viz1564690518427');
  var vizElement = divElement.getElementsByTagName('object')[0];
  vizElement.style.width='1016px';vizElement.style.height='991px';
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);        