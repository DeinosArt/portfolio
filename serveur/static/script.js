function getSearchInputValue(){
    var value = document.getElementById("Search").value
    return value
}

// run on page load
var searchInput = $("#Search")
searchInput[0].value = "";

var filtrableImages = $(".filtrable")

function display(index, jsImageContainer){
    var imageContainer = $(jsImageContainer)
    //console.info("image", imageContainer, "index", index, "type", typeof(imageContainer))
    var alt = imageContainer.attr("data-tag")
    var value = getSearchInputValue();
    if(String(alt).includes(value) || value == "" ){
        imageContainer.removeClass("d-none");
    }
    else{
        imageContainer.addClass("d-none");
    }
}

function realTimeDisplay(){
    filtrableImages.each(display) 
}

searchInput.on('input', realTimeDisplay);
$("#bouton").on('click', realTimeDisplay);