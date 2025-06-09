// static/liff/explain.js

document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/explain")
    .then((response) => response.json())
    .then((data) => {
      // 顯示建議文字
      document.getElementById("suggestion").textContent = `✅ 建議：${data.suggestion}`;

      // 顯示理由（用列表列出）
      const reasonsList = document.getElementById("reasons");
      reasonsList.innerHTML = "";
      data.reasoning.forEach((r) => {
        const li = document.createElement("li");
        li.textContent = r;
        reasonsList.appendChild(li);
      });
    })
    .catch((error) => {
      console.error("❌ explain API 請求失敗：", error);
    });
});
