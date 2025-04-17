document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        const nameInput = document.getElementById("name");
        const capitalInput = document.getElementById("capital");
        const populationInput = document.getElementById("population");
        const regionInput = document.getElementById("region");
        const descriptionInput = document.getElementById("description");
        const imageInput = document.getElementById("image");

        form.addEventListener("submit", function (event) {
            let valid = true;

            if (nameInput.value.trim() === "") {
                alert("Please enter a country name.");
                valid = false;
            }

            if (capitalInput.value.trim() === "") {
                alert("Please enter a capital.");
                valid = false;
            }
            if (isNaN(populationInput.value) ||
                populationInput.value.trim() === "" ||
                Number(populationInput.value) < 0
            ) {
                alert("Please enter a valid population number (positive only).");
                valid = false;
            }

            if (regionInput.value.trim() === "") {
                alert("Please enter a region.");
                valid = false;
            }

            if (descriptionInput.value.trim() === "") {
                alert("Please enter a description.");
                valid = false;
            }

            const fileExtension = imageInput.value.split('.').pop().toLowerCase();
            const allowedExtensions = ["png", "jpg", "jpeg", "gif"];
            if (!allowedExtensions.includes(fileExtension)) {
                alert("Please upload a valid image (JPG, PNG, or GIF).");
                valid = false;
            }

            if (!valid) {
                event.preventDefault();
            }
        });
    }

    document.querySelectorAll(".read-toggle").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const shortDesc = link.parentElement.querySelector(".short-desc");
            const fullDesc = link.parentElement.querySelector(".full-desc");

            if (fullDesc.classList.contains("d-none")) {
                shortDesc.classList.add("d-none");
                fullDesc.classList.remove("d-none");
                link.textContent = "Read less";
            } else {
                shortDesc.classList.remove("d-none");
                fullDesc.classList.add("d-none");
                link.textContent = "Read more";
            }
        });
    });
});
