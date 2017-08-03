(function(){

	let xhr=new XMLHttpRequest(); 

	xhr.onreadystatechange=function(){
		if(xhr.readyState==4){
			if((xhr.status>=200 && xhr.status<300)||xhr.status==304){
			
				responseObj=JSON.parse(xhr.responseText);
				if(responseObj.status=="ok"){
					alert("add success");
					let studentListWrapper=document.getElementById("student-list-wrapper");
					studentListWrapper.innerHTML=responseObj.studentListRendering;
				}else{
					alert("add failed");
				}

			}else{
				alert("response failed");
			}
		}
	}

	let addBtn=document.getElementById("id_addBtn");

	addBtn.addEventListener("click",function(){

		xhr.open("post","add/",true);

		let username=document.getElementById("id_username").value;
		let age=document.getElementById("id_age").value;

		let msg=JSON.stringify({"username":username,"age":age});

		xhr.send(msg);
	});

	
})();