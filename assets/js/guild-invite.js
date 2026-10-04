(() => {
  const invite = document.getElementById("guild-invite");
  if (!invite) return;

  const cookieName = "frostborn-invite-dismissed";
  const closeButton = invite.querySelector("button");

  // Start hidden so a remembered dismissal never flashes during page loading.
  try {
    invite.hidden = document.cookie.split(";").some(
      (cookie) => cookie.trim() === `${cookieName}=1`
    );
  } catch {
    invite.hidden = false;
  }

  closeButton.addEventListener("click", () => {
    invite.hidden = true;
    if (document.activeElement === closeButton) {
      document.querySelector(".site-title")?.focus({ preventScroll: true });
    }

    try {
      const secure = location.protocol === "https:" ? "; Secure" : "";
      document.cookie = `${cookieName}=1; Max-Age=31536000; Path=/; SameSite=Lax${secure}`;
    } catch {
      // Dismissal still works for this page when browser cookies are unavailable.
    }
  });
})();
