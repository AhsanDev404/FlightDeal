window.onload = function () {
  const toastTrigger = document.getElementById("liveToastBtn_flightdetails");
  const toastLiveExample = document.getElementById("liveToast_flightdetails");
  if (toastTrigger) {
    toastTrigger.addEventListener("click", () => {
      const toast = new bootstrap.Toast(toastLiveExample);

      toast.show();
    });
  }


const packageTrigger = document.getElementById("liveToastBtn_packagedetails");
  const packagetoastLive = document.getElementById("liveToast_packagedetails");
  if (packageTrigger) {
    packageTrigger.addEventListener("click", () => {
      const toast = new bootstrap.Toast(packagetoastLive);

      toast.show();
    });
  }

};

