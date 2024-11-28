function confirmDelete() {
    return confirm("Are you sure you want to delete this flashcard?");
}
function toggleAnswer(flashcardElement) {
    const answerElement = flashcardElement.querySelector('.answer');
    // Toggle the display of the answer
    answerElement.style.display = (answerElement.style.display === "none") ? "block" : "none";
}


function deleteCategory(category) {
    return confirm(`Are you sure you want to delete the category "${category}" and all its flashcards?`);
}