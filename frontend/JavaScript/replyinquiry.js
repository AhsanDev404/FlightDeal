window.onload = function () {
  const repTrigger1 = document.getElementById("liveToastBtn_replyinquiry1");
  const reptoastLive1 = document.getElementById("liveToast_replyinquiry1");
  if (repTrigger1) {
    repTrigger1.addEventListener("click", () => {
      const toast = new bootstrap.Toast(reptoastLive1);

      toast.show();
    });
  }


  const repTrigger2 = document.getElementById("liveToastBtn_replyinquiry2");
  const reptoastLive2 = document.getElementById("liveToast_replyinquiry2");
  if (repTrigger2) {
    repTrigger2.addEventListener("click", () => {
      const toast = new bootstrap.Toast(reptoastLive2);

      toast.show();
    });
  }


  const repTrigger3 = document.getElementById("liveToastBtn_replyinquiry3");
  const reptoastLive3 = document.getElementById("liveToast_replyinquiry3");
  if (repTrigger3) {
    repTrigger3.addEventListener("click", () => {
      const toast = new bootstrap.Toast(reptoastLive3);

      toast.show();
    });
  }

};

