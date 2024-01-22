console.log("ups");

function commentUp(postId, username){
    console.log(username)
    const url="/write_comment/";
    const httpRequest=new XMLHttpRequest();
    httpRequest.open("POST",url,true),
    httpRequest.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    const element=document.querySelector(`.comment-write-${postId}`);
    const text=element.value;
    console.log();
    if(text==null || text==""){
        console.log("error")
        return
    }
    httpRequest.send(JSON.stringify({id:postId, comment:text}));

    function onComplete(){
        if(httpRequest.readyState===XMLHttpRequest.DONE){
            if(httpRequest.status<400){
                
                const {id,text,comment_id}=JSON.parse(httpRequest.response);
                const new_container = document.createElement("div");
                new_container.className="comment-container";
                new_container.id=`comment-${id}-${comment_id}`;
                const user="<strong>"+username+" </strong>"
                const new_comment = document.createElement("p");
                new_comment.innerHTML=user+text;
                const delete_button = document.createElement("button");
                delete_button.type="button";
                delete_button.innerText="삭제";
                delete_button.setAttribute("onclick",`delete_comment(${id},${comment_id})`);
                new_container.appendChild(new_comment);
                new_container.appendChild(delete_button);  
                
                console.log(new_container);
                const element=document.querySelector(`.post-${id}-comment`);
                
                element.appendChild(new_container);
                const box=document.querySelector(`.comment-write-${postId}`);
                box.value=null;
            }
        }
        else{
            const box=document.querySelector(`.comment-write-${postId}`);
            box.value=null;
        }
    }
    httpRequest.onreadystatechange=onComplete;
}


function change_like(postId){
    console.log(postId);
    const url="/change_like/";
    const httpRequest=new XMLHttpRequest();
    httpRequest.open("POST",url,true),
    httpRequest.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    const element=document.querySelector(`#like-num-${postId}`);
    const cbox=document.querySelector(`#myCheck-${postId}`);
    console.log(cbox);
    if(cbox.checked){
        console.log("checked");
        httpRequest.send(JSON.stringify({id:postId, num:-1}));
    }
    else{
        console.log("not");
        httpRequest.send(JSON.stringify({id:postId, num:1}));
    }

    function onComplete(){
        if(httpRequest.readyState===XMLHttpRequest.DONE){
            if(httpRequest.status<400){
                const {id, num}=JSON.parse(httpRequest.response);
                const text=element.outerText;
                console.log(text);
                element.innerText=num;
            }
        }
        else{
            
        }
    }
    httpRequest.onreadystatechange=onComplete;
}

function delete_comment(postId, commentId){
    console.log(postId);
    const url="/delete_comment/";
    const httpRequest=new XMLHttpRequest();
    httpRequest.open("POST",url,true),
    httpRequest.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    httpRequest.send(JSON.stringify({pid:postId, cid:commentId}));

    function onComplete(){
        if(httpRequest.readyState===XMLHttpRequest.DONE){
            if(httpRequest.status<400){
                const {id}=JSON.parse(httpRequest.response);
                const element=document.querySelector(`#comment-${postId}-${commentId}`);
                element.remove();
            }
        }
        else{
            
        }
    }
    httpRequest.onreadystatechange=onComplete;
}