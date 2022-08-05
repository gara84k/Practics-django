const $del = document.querySelectorAll(".btnDelete");

(() => {
  $del.forEach(function (btn) {
    btn.addEventListener("click", (e) => {
      let confirmation = confirm(
        "🤗Are you sure you want to delete this activity?🤔"
      );
      if (!confirmation) e.preventDefault();
    });
  });
})();
