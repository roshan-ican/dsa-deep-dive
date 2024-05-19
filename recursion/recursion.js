function takeShower() {
  console.log("Showering");
  return "Showering!";
}

function eatBreakfast() {
  let meal = cookFood();
  console.log(`Eating ${meal}`);
  return `Eating ${meal}`;
}

function cookFood() {
  let items = ["Steak", "Biryani", "Egg Noodles", "Sushi"];
  return items[Math.floor(Math.random() * items.length)];
}
function wakeUp() {
  takeShower();
  eatBreakfast();
  console.log("Ok we are ready to go!");
}

wakeUp();

// Count down
function countDown(num) {
  if (num <= 0) {
    console.log("All done");
    return;
  }
  console.log(num);
  num--;
  countDown(num);
}
console.log(
  "🚀 ~ file: recursion.js:34 ~ countDown ~ countDown:",
  countDown(5)
);
