const TICKET_SNIPPETS = document.querySelectorAll(".ticket-snippet")

// add ticket events on buttons edit / delete
for(var i = 0; i < TICKET_SNIPPETS.length; i++){

    const PK = TICKET_SNIPPETS[i].id
    const REVIEW_BUTTON = TICKET_SNIPPETS[i].querySelector(".review-button")

    try{
        // edit ticket button
        REVIEW_BUTTON.onclick = function(){
            location.href = "/new_review/" + PK
        }        
    }
    catch{

    }
}
