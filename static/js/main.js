const option1 = document.getElementById("who-option-1");
const option2 = document.getElementById("who-option-2");
const option3 = document.getElementById("who-option-3");

const transitionYoungLearner = document.getElementById("transition-section-1");
const transitionStudent = document.getElementById("transition-section-2");
const transitionCareerChanger = document.getElementById("transition-section-3");



option1.onclick = function () {
    if (transitionYoungLearner.style.display !== "contents") {
      transitionYoungLearner.style.display = "contents";
    }
    option2.style.display = "none";
    option3.style.display = "none"
  };

option2.onclick = function () {
    if (transitionStudent.style.display !== "contents") {
      transitionStudent.style.display = "contents";
    }

    option1.style.display = "none";
    option3.style.display = "none"
  };

option3.onclick = function () {
    if (transitionCareerChanger.style.display !== "contents") {
      transitionCareerChanger.style.display = "contents";
    }

    option1.style.display = "none";
    option2.style.display = "none"
  };