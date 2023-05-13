// Placeholder API call function
  function updateUserThemePreference(theme) {
    $.ajax({
      url: '/api/set_theme',
      type: 'POST',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({ theme: theme }),
      success: function(data) {
        console.log(data);
        localStorage.setItem('theme', theme);
      },
      error: function(err) {
        console.log(err);
      },
    });
  }

  function updateTheme(theme) {
    $('html').attr('data-bs-theme', theme);
    $('#flexSwitchCheckDefault').prop('checked', theme === 'light');
    $('label[for="flexSwitchCheckDefault"]').text(theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
  }

  $(document).ready(function () {
    let isLoggedIn = false;
  
    // First, get the theme from local storage (or use 'dark' if none is set)
    let theme = localStorage.getItem('theme') || 'dark';
    updateTheme(theme);

    $.ajax({
      url: '/api/logged_in',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        isLoggedIn = true; // User is logged in
        theme = data.theme; // Set the theme from user data
        localStorage.setItem('theme', theme); // Update local storage
        updateTheme(theme); // Update the theme based on server's response
      },
      error: function(err) {
        console.log(err);
      },
    });
  
    $('#flexSwitchCheckDefault').on('change', function () {
      const isChecked = $(this).is(':checked');
      theme = isChecked ? 'light' : 'dark';
  
      updateTheme(theme);
      localStorage.setItem('theme', theme); // Update local storage on switch change
  
      if (isLoggedIn) {
        updateUserThemePreference(theme);
      }
    });
  });