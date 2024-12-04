const myList = [
    "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
    "Bahrain", "Bangladesh", "Belarus", "Belgium", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil", 
    "Bulgaria", "Cameroon", "Canada", "Chile", "China", "Colombia", "Congo Republic", "Costa Rica", "Croatia", 
    "Cyprus", "Czech Republic", "Denmark", "Ecuador", "Egypt", "El Salvador", "England", "Estonia", "Faroe Islands", 
    "Finland", "France", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Guatemala", "Honduras", "Hong Kong", 
    "Hungary", "Iceland", "India", "Indonesia", "Iran", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", 
    "Japan", "Jordan", "Kazakhstan", "Kenya", "Kosovo", "Kuwait", "Latvia", "Lebanon", "Liechtenstein", "Lithuania", 
    "Luxembourg", "Malaysia", "Malta", "Mexico", "Moldova", "Montenegro", "Morocco", "Myanmar", "Netherlands", 
    "New Zealand", "Nicaragua", "Nigeria", "North Macedonia", "Northern Ireland", "Norway", "Oman", "Pakistan", 
    "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", 
    "Rwanda", "San Marino", "Saudi Arabia", "Scotland", "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", 
    "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Tanzania", "Thailand", "Trinidad and Tobago", 
    "Tunisia", "Turkey", "Uganda", "Ukraine", "United Arab Emirates", "Uruguay", "USA", "Uzbekistan", "Venezuela", 
    "Vietnam", "Wales", "Zambia", "Zimbabwe"
];

// Function to shuffle the array using CSPRNG
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        // Get a cryptographically secure random index
        const j = crypto.getRandomValues(new Uint32Array(1))[0] % (i + 1);
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    }
}

// Shuffle the list
shuffleArray(myList);

// Print the shuffled list with numbering
console.log("");
myList.forEach((country, index) => {
    console.log(`${index + 1}  ${country}`);
});

console.log("");
console.log(myList);
console.log("");
