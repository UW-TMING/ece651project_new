function $(id){
	return typeof id==='string'?document.getElementById(id):id;
}
window.onload=tab;
function tab(){
  var lis=$('login-nav').getElementsByTagName('li');
  var divs=$('content').getElementsByTagName('div');
 
  for(var i=0;i<lis.length;i++){
    lis[i].id=i;
    lis[i].onmouseover=function(){
    	for(var j = 0; j<lis.length; j++){
    		lis[j].className = '';
    		divs[j].style.display = 'none';
    	} 
        this.className = "select";
        divs[this.id].style.display = "block";
    }
  }
}