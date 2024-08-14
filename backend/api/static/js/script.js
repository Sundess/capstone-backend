document.addEventListener("DOMContentLoaded", function () {
  // const loginForm = document.querySelector(".login-form form");
  // const signUpForm = document.querySelector(".sign-up-form form");
  // const flipContainer = document.querySelector(".flip-container");
  // const helpButton = document.querySelector(".help-button");
  // const privacyButton = document.querySelector(".info-button");
  // const communityButton = document.querySelector(".more-button");
  // const backButton = document.getElementById("back-button");
  // const modal = document.getElementById("modal");
  // const container = document.querySelector(".container");
  // const helpImage = document.querySelector(".help-image");
  // const privacyImage = document.querySelector(".Privacy-image");
  // const communityImage = document.querySelector(".Community-image");
  // // Hide all images initially
  // const hideAllImages = () => {
  //   helpImage.style.display = "none";
  //   privacyImage.style.display = "none";
  //   communityImage.style.display = "none";
  // };

  // hideAllImages(); // Initial hiding of images

  // // Get CSRF token from cookies
  // function getCookie(name) {
  //   let cookieValue = null;
  //   if (document.cookie && document.cookie !== "") {
  //     const cookies = document.cookie.split(";");
  //     for (let i = 0; i < cookies.length; i++) {
  //       const cookie = cookies[i].trim();
  //       if (cookie.substring(0, name.length + 1) === name + "=") {
  //         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
  //         break;
  //       }
  //     }
  //   }
  //   return cookieValue;
  // }

  // const csrftoken = getCookie("csrftoken");

  // // Login Form Submission
  // loginForm.addEventListener("submit", function (event) {
  //   event.preventDefault();
  //   const username = document.getElementById("username").value;
  //   const password = document.getElementById("password").value;

  //   if (username && password) {
  //     // User credentials
  //     const loginData = {
  //       username: username,
  //       password: password,
  //     };
  //     // Make the POST request using fetch
  //     function getCookie(name) {
  //       let cookieValue = null;
  //       if (document.cookie && document.cookie !== "") {
  //         const cookies = document.cookie.split(";");
  //         for (let i = 0; i < cookies.length; i++) {
  //           const cookie = cookies[i].trim();
  //           // Does this cookie string begin with the name we want?
  //           if (cookie.substring(0, name.length + 1) === name + "=") {
  //             cookieValue = decodeURIComponent(
  //               cookie.substring(name.length + 1)
  //             );
  //             break;
  //           }
  //         }
  //       }
  //       return cookieValue;
  //     }

  //     const csrftoken = getCookie("csrftoken");

  //     fetch("http://127.0.0.1:8000/api-auth/login/", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //         "X-CSRFToken": csrftoken, // Include the CSRF token in the headers
  //       },
  //       body: JSON.stringify(loginData),
  //     })
  //       .then((response) => {
  //         if (!response.ok) {
  //           throw new Error(
  //             "Network response was not ok " + response.statusText
  //           );
  //         }
  //         return response.json();
  //       })
  //       .then((data) => {
  //         console.log("Success:", data);
  //       })
  //       .catch((error) => {
  //         console.error("Error:", error);
  //       });
  //   } else {
  //     alert("Please enter both username and password");
  //   }
  // });

  // // Sign-Up Form Submission
  // signUpForm.addEventListener("submit", function (event) {
  //   event.preventDefault();
  //   const username = document.getElementById("username").value;
  //   const email = document.getElementById("email").value;
  //   const password = document.getElementById("password").value;
  //   const confirmPassword = document.getElementById("confirm-password").value;

  //   if (username && email && password && password === confirmPassword) {
  //     alert("Sign Up Successful");
  //   } else {
  //     alert("Please fill all fields correctly");
  //   }
  // });

  const handleFlip = () => {
    if (flipContainer.classList.contains("flip")) {
      flipContainer.classList.remove("flip");
    } else {
      flipContainer.classList.add("flip");
    }
  };

  document.querySelectorAll(".flip-toggle").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      handleFlip();
    });
  });

  if (window.location.pathname.includes("signup.html")) {
    flipContainer.classList.add("flip");
  } else if (window.location.pathname.includes("login.html")) {
    flipContainer.classList.remove("flip");
  }

  // Modal functionality
  const showModal = (imageElement) => {
    hideAllImages();
    imageElement.style.display = "block";
    modal.style.display = "flex";
    container.classList.add("blurred");
  };

  helpButton.addEventListener("click", () => {
    showModal(helpImage);
  });

  privacyButton.addEventListener("click", () => {
    showModal(privacyImage);
  });

  communityButton.addEventListener("click", () => {
    showModal(communityImage);
  });

  backButton.addEventListener("click", () => {
    modal.style.display = "none";
    container.classList.remove("blurred");
  });
});
