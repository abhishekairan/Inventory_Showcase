
document.addEventListener("DOMContentLoaded", function() {
    const rows = document.querySelectorAll(".project-table tbody tr");
    // console.log(rows)
    rows.forEach(row => {
        row.addEventListener("click", function() {
            // console.log("Clicked")
            const url = row.getAttribute("data-url");
            console.log(url)
            if (url) {
                window.location.href = url;
            }
        });
    });
});
