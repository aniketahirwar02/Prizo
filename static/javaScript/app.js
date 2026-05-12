function searchProduct() {

    const searchValue = document
        .getElementById("searchBox")
        .value;

    // Redirect to result page
    window.location.href =
        `/result?query=${searchValue}`;
}
