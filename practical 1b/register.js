document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
  
    const user = { name, email, password };
  
    // Get existing users from localStorage or create new array
    const users = JSON.parse(localStorage.getItem('users')) || [];
  
    // Push new user and save back to localStorage
    users.push(user);
    localStorage.setItem('users', JSON.stringify(users));
  
    // AJAX POST request (replace URL with your server endpoint)
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://jsonplaceholder.typicode.com/posts', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 201) {
        console.log('User registered:', xhr.responseText);
        window.location.href = 'user-list.html';
      }
    };
    xhr.send(JSON.stringify(user));
  });
  