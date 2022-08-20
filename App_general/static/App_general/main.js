console.log('Oni Delivery');

const subscriptionformJS = document.querySelector('.subscription-formJS');

function foodSetValidation(event){
    const checkFoodSelect = document.querySelectorAll('input[name="food_set"]:checked');
    if (checkFoodSelect.length === 0){
        event.preventDefault();
        alert('Please select 1 menu mother fuckerrrrrr !!!')
    }
}

if (!!subscriptionformJS){
    subscriptionformJS.addEventListener('submit', foodSetValidation);
}
