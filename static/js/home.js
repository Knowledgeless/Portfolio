document.addEventListener("DOMContentLoaded", () => {
  const textEl = document.querySelector(".typed-text");
  const cursor = document.querySelector(".cursor");
  const words = ["Web Developer", "Graphics Designer"];
  let i = 0, j = 0, isDeleting = false;

  function type() {
    const current = words[i];
    const displayed = current.substring(0, j);
    textEl.textContent = displayed;

    if (!isDeleting && j < current.length) {
      j++;
      setTimeout(type, 120);
    } else if (isDeleting && j > 0) {
      j--;
      setTimeout(type, 60);
    } else {
      isDeleting = !isDeleting;
      if (!isDeleting) i = (i + 1) % words.length;
      setTimeout(type, 1000);
    }
  }
  type();
});
