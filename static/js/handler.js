// Placeholder API call function
function updateUserThemePreference(theme) {
    // Implement API call to save the user's theme preference in the database.
    console.log("API call to update user's theme preference to:", theme);
  }

  $(document).ready(function () {
    const isLoggedIn = false; // Replace this with a check for the user's login status.
  
    // Get theme preference from local storage or use the default theme.
    const defaultTheme = 'dark';
    let theme = isLoggedIn ? null : localStorage.getItem('theme') || defaultTheme;
  
    if (theme) {
      $('html').attr('data-bs-theme', theme);
      $('#flexSwitchCheckDefault').prop('checked', theme === 'light');
      $('label[for="flexSwitchCheckDefault"]').text(theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    }
  
    $('#flexSwitchCheckDefault').on('change', function () {
      const htmlElement = $('html');
      const labelElement = $('label[for="flexSwitchCheckDefault"]');
      const isChecked = $(this).is(':checked');
  
      theme = isChecked ? 'light' : 'dark';
  
      htmlElement.attr('data-bs-theme', theme);
      labelElement.text(isChecked ? 'Switch to dark theme' : 'Switch to light theme');
  
      if (isLoggedIn) {
        updateUserThemePreference(theme);
      } else {
        localStorage.setItem('theme', theme);
      }
    });
  });