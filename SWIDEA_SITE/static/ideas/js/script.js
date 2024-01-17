// get url query string
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

// 정렬방식 셀렉트 박스 유지
$(document).ready(function(){
  var sort = getUrlParameter('sort');
  if(sort == 'olddate'){
    $('.sort-olddate').prop('selected', 'selected')
  }else if(sort == 'title'){
    $('.sort-title').prop('selected', 'selected')
  }else if(sort == 'newdate'){
    $('.sort-newdate').prop('selected', 'selected')
  }else{
    $('.sort-interest').prop('selected', 'selected')
  }
});

// const plus_button=document.getElementById("plus_interest");
// const interest=document.getElementById("interest_now");
// const minus_button=document.getElementById("minus_interest")
// console.log(1)
// plus_button.addEventListener("click",(e)=>{
//   let now=parseInt(interest.innerText);
//   console.log(now+1);
//   now+=1;
//   interest.
//   interest.outerText(now);
// })

// JavaScript
var interestLevel = document.getElementById("interest-level");
var plusButton = document.getElementById("plus");
var minusButton = document.getElementById("minus");


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let originalDisplayStyle;

function showStar(id) {
    const star = document.getElementById("star-"+id);
    originalDisplayStyle = star.style.display;
    star.style.display = "block";
}

function hideStar(id) {
    const star = document.getElementById("star-"+id);
    star.style.display = originalDisplayStyle;
}

function toggleFavorite(id) {
    const star = document.getElementById("star-"+id);
    if(originalDisplayStyle=="block"){
      star.style.display="none"
      console.log("찜하기 해제!");
      originalDisplayStyle = star.style.display;
      now="False"
    }
    else{
      star.style.display="block"
      console.log("찜하기!");
      originalDisplayStyle = star.style.display;
      now="True"
    }
    
    $.ajax({
      url: '/change_heart/', // URL 인코딩
      data: jQuery.param({heart:now, id:id}) ,
      method: 'POST',
      dataType: 'json',
      headers: {
          'X-CSRFToken': csrftoken
      },
      success: function (data) {
        console.log("success");
      },
      error: function (error) {
          console.log('Error:', error);
      }
    });
}