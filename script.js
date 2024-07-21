document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = form.elements['name'].value;
        const email = form.elements['email'].value;
        const message = form.elements['message'].value;

        if (name && email && message) {
            alert(`Gracias, ${name}. Hemos recibido tu mensaje.`);
            form.reset();
        } else {
            alert('Por favor, completa todos los campos.');
        }
    });
});
