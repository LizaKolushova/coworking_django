const accordionHeaders = document.getElementsByClassName('accordion__header');

for (const accordionHeader of accordionHeaders) {
    if (accordionHeader.parentElement.classList.contains('accordion__item--active')) {
        const accordionBody = accordionHeader.nextElementSibling;
        accordionBody.style.maxHeight = accordionBody.style.maxHeight ? null : accordionBody.scrollHeight + 'px';
    }

    accordionHeader.addEventListener('click', function () {
        const accordionItem = this.parentElement;
        accordionItem.classList.toggle('accordion__item--active')
        const accordionBody = this.nextElementSibling;
        accordionBody.style.maxHeight = accordionBody.style.maxHeight ? null : accordionBody.scrollHeight + 'px';
    });
}

document.querySelector('.header-toggler').addEventListener('click', function () {
    this.classList.toggle('open');
    const navbar = this.nextElementSibling;
    navbar.style.maxHeight = navbar.style.maxHeight ? null : navbar.scrollHeight + 'px';
});
const sendForm = document.getElementById('sendForm');
        sendForm.addEventListener('submit', function (event) {
            event.preventDefault();

            this.classList.add('was-validated');

            if (!this.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                return;
            }

            new FormData(this);
        }, false);
        sendForm.addEventListener('formdata', function (event) {
            let sendFormData = {};
            for (const [key, value] of event.formData.entries()) {
                sendFormData[key] = value;
            }
            console.table(sendFormData);
        });