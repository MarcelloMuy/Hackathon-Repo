window.onload = function(){ 

  const whoSection = document.getElementById("who-section")

  const option1 = document.getElementById("who-option-1");
  const option2 = document.getElementById("who-option-2");
  const option3 = document.getElementById("who-option-3");

  // YOUNG LEARNER VARIABLES
  const transitionYoungLearner = document.getElementById("transition-section-1");

  const transitionYoungLearnerInfo = document.getElementById("transition-ul-1");
  const transitionYoungLearnerImage = document.getElementById("transition-image-1")

  const transitionYoungLearnerIconCircle = document.getElementById("transition-icon-circle-1")
  const transitionYoungLearnerIconTick = document.getElementById("transition-icon-tick-1")

  // STUDENT VARIABLES
  const transitionStudent = document.getElementById("transition-section-2");

  const transitionStudentInfo = document.getElementById("transition-ul-2");
  const transitionStudentImage = document.getElementById("transition-image-2")

  const transitionStudentIconCircle = document.getElementById("transition-icon-circle-2")
  const transitionStudentIconTick = document.getElementById("transition-icon-tick-2")

  // CAREER CHANGER VARIABLES
  const transitionCareerChanger = document.getElementById("transition-section-3");

  const transitionCareerChangerInfo = document.getElementById("transition-ul-3");
  const transitionCareerChangerImage = document.getElementById("transition-image-3")

  const transitionCareerChangerIconCircle = document.getElementById("transition-icon-circle-3")
  const transitionCareerChangerIconTick = document.getElementById("transition-icon-tick-3")



  option1.onclick = function () {
      whoSection.scrollIntoView();
      if (transitionYoungLearner.style.display !== "contents") {
        transitionYoungLearner.style.display = "contents";
        transitionYoungLearnerInfo.classList.add("animate__animated", "animate__bounceInRight");
        transitionYoungLearnerImage.classList.add("animate__animated", "animate__bounceInLeft");

        transitionYoungLearnerIconCircle.style.display = "none";
        transitionYoungLearnerIconCircle.style.color = "green";
        transitionYoungLearnerIconTick.style.display = "contents";


        option2.classList.add("animate__animated", "animate__bounceOutRight");
        option3.classList.add("animate__animated", "animate__bounceOutRight");
      }

      setInterval(
        function(){
          option2.style.display = "none";
          option3.style.display = "none";
        },
        1000
      );
      
      
    };
  option2.onclick = function () {
      whoSection.scrollIntoView();
      if (transitionStudent.style.display !== "contents") {
        transitionStudent.style.display = "contents";
        transitionStudentInfo.classList.add("animate__animated", "animate__bounceInRight");
        transitionStudentImage.classList.add("animate__animated", "animate__bounceInLeft");

        transitionStudentIconCircle.style.display = "none";
        transitionStudentIconCircle.style.color = "green";
        transitionStudentIconTick.style.display = "contents";


        option1.classList.add("animate__animated", "animate__bounceOutRight");
        option3.classList.add("animate__animated", "animate__bounceOutRight");
      }

      setInterval(
        function(){
          option1.style.display = "none";
          option3.style.display = "none";
        },
        1000
      );
      
      
    };
  option3.onclick = function () {
      whoSection.scrollIntoView();
      if (transitionCareerChanger.style.display !== "contents") {
        transitionCareerChanger.style.display = "contents";
        transitionCareerChangerInfo.classList.add("animate__animated", "animate__bounceInRight");
        transitionCareerChangerImage.classList.add("animate__animated", "animate__bounceInLeft");

        transitionCareerChangerIconCircle.style.display = "none";
        transitionCareerChangerIconCircle.style.color = "green";
        transitionCareerChangerIconTick.style.display = "contents";


        option1.classList.add("animate__animated", "animate__bounceOutRight");
        option2.classList.add("animate__animated", "animate__bounceOutRight");
      }

      setInterval(
        function(){
          option1.style.display = "none";
          option2.style.display = "none";
        },
        1000
      );
      
      
    };
};
