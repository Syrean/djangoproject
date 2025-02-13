ScrollReveal({
    distance: "100px",
  });
  
  ScrollReveal().reveal(".nav-bar", { delay: 100, origin: "top" });
  ScrollReveal().reveal("#experience, #skills, #about, #contact", {
    delay: 300,
    origin: "left",
  });
  ScrollReveal().reveal(".profile, .contacts", { delay: 300, origin: "left" });
  ScrollReveal().reveal(".name, .skills, .social", {
    delay: 300,
    origin: "right",
  });
  ScrollReveal().reveal(".experience, .about", { delay: 300 });
  ScrollReveal().reveal(".list", { interval: 200 });
  
  var prevScrollpos = window.pageYOffset;
  
  var prevScrollpos = window.pageYOffset;
  
  window.addEventListener("scroll", function () {
    var currentScrollPos = window.pageYOffset;
    console.log("Previous: " + prevScrollpos + ", Current: " + currentScrollPos); // Debugging
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-125px";
    }
    prevScrollpos = currentScrollPos;
  });
  
  // Get the button
  let mybutton = document.getElementById("bt-up");
  
  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function () {
    scrollFunction();
  };
  
  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  
  // When the user clicks on the button, scroll to the top of the document
  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
  