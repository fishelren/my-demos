let btn=document.getElementById("request-data-btn");
let elem=document.getElementById("content");
btn.addEventListener("click",function(){
	let xhr=new XMLHttpRequest();
	xhr.onreadystatechange=function(){
		if(xhr.readyState==4){
			if((xhr.status>=200 && xhr.status<300) || xhr.status==304){
				let data=JSON.parse(xhr.responseText);
				elem.innerHTML=data.list2.join(" ");
			}else{
				console.log("error");
			}
		}
	}
	xhr.open("get","/get_data",true);
	xhr.send(null);
});