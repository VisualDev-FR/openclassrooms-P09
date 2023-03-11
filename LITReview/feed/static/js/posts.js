const REVIEW_SNIPPETS = document.querySelectorAll(".review-snippet")
const TICKET_SNIPPETS = document.querySelectorAll(".ticket-snippet")


// add reviews events on buttons edit / delete
for(var i = 0; i < REVIEW_SNIPPETS.length; i++){

    const PK = REVIEW_SNIPPETS[i].id

    const EDIT_BUTTON = REVIEW_SNIPPETS[i].querySelector(".edit-button")
    const DELETE_BUTTON = REVIEW_SNIPPETS[i].querySelector(".delete-button")

    EDIT_BUTTON.onclick = (e) => {
        location.href = "/edit_review/" + PK
    }

    DELETE_BUTTON.onclick = (e) => {
        if(confirm("Voulez-vous supprimer cette critique ?")){
            location.href = "/delete_review/" + PK
        }  
    }
}


// add ticket events on buttons edit / delete
for(var i = 0; i < TICKET_SNIPPETS.length; i++){

    const PK = TICKET_SNIPPETS[i].id

    const EDIT_BUTTON = TICKET_SNIPPETS[i].querySelector(".edit-button")
    const DELETE_BUTTON = TICKET_SNIPPETS[i].querySelector(".delete-button")

    EDIT_BUTTON.onclick = (e) => {
        location.href = "/edit_ticket/" + PK
    }

    DELETE_BUTTON.onclick = (e) => {
        if(confirm("Voulez-vous supprimer ce ticket ?")){
            location.href = "/delete_ticket/" + PK
        }        
    }
}