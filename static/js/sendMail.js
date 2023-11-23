// JS Function from Bootstrap Resume walkthough 

function sendMail(contactForm) {
    emailjs.send("service_1n6flmt", "template_cx2tzzb", {
        "from_name": contactForm.name.value, 
        "from_email": contactForm.email.value,
        "from_phone": contactForm.phone.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
}