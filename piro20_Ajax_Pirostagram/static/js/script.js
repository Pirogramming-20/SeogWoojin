console.log("ups");

function commentUp(postId){
    console.log(postId)
    const url="/write_comment/";
    const httpRequest=new XMLHttpRequest();
    httpRequest.open("POST",url,true),
    httpRequest.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    const element=document.querySelector(`.comment-write-${postId}`);
    const text=element.value;
    console.log(typeof(text));
    httpRequest.send(JSON.stringify({id:postId, comment:text}));

    function onComplete(){
        if(httpRequest.readyState===XMLHttpRequest.DONE){
            if(httpRequest.status<400){
                const {id,text}=JSON.parse(httpRequest.response);
                const element=document.querySelector(`.post-${id}-comment`);
                const originHTML =element.innerHTML;
                console.log(text);
                const new_comment = document.createElement("p");
                console.log(new_comment);
                new_comment.innerHTML=text;
                console.log(new_comment)
                element.appendChild(new_comment);
            }
        }
        else{
    
        }
    }
    httpRequest.onreadystatechange=onComplete;
}

