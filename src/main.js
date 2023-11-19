document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('addDetailButton').addEventListener('click', addDetailField);
    document.getElementById('contactForm').addEventListener('submit', submitForm);
});

function addDetailField() {
    const detailContainer = document.getElementById('additionalDetails');

    // Create a dropdown for detail type
    const detailType = document.createElement('select');
    detailType.innerHTML = `<option value="">Select Detail</option>
                            <option value="phone">Phone Number</option>
                            <option value="birthday">Birthday</option>
                            <option value="other">Other</option>`;
    detailType.onchange = () => handleDetailTypeChange(detailType, detailContainer);
    
    detailContainer.appendChild(detailType);
}

function handleDetailTypeChange(selectElement, container) {
    // Remove any existing input field
    let nextElement = selectElement.nextSibling;
    while(nextElement) {
        container.removeChild(nextElement);
        nextElement = selectElement.nextSibling;
    }

    // Add new input field based on selection
    if (selectElement.value === 'other') {
        createInputField('text', 'Specify Detail Type', container);
    }
    createInputField('text', 'Detail Description', container);
}

function createInputField(type, placeholder, container) {
    const inputField = document.createElement('input');
    inputField.type = type;
    inputField.placeholder = placeholder;
    inputField.name = placeholder.replace(/\s+/g, '').toLowerCase();
    container.appendChild(inputField);
}

function submitForm(event) {
    event.preventDefault();

    // Collect data from form fields
    const formData = new FormData(event.target);
    const formObject = {};
    formData.forEach((value, key) => {
        if (formObject.hasOwnProperty(key)) {
            formObject[key] = [...formObject[key], value];
        } else {
            formObject[key] = value;
        }
    });

    // Send data to backend
    fetch('/submit_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formObject)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}