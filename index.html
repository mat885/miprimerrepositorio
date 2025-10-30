<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Proyecto-carbono</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    header {
      display: flex;
      justify-content: space-between;
      background-color: #e0f7fa;
      padding: 10px 20px;
    }
    #main { text-align: center; margin-top: 50px; }
    button { margin: 10px; padding: 10px 20px; }
    .hidden { display: none; }
    form { margin-top: 20px; }
    input { display: block; margin: 5px auto; padding: 8px; width: 80%; max-width: 300px; }
  </style>
</head>
<body>

  <header>
    <button onclick="calcular()">Calcular</button>
    <div id="userArea">
      <button onclick="mostrarLogin()">Iniciar sesión</button>
    </div>
  </header>

  <div id="main">
    <h1>Bienvenido a Proyecto-carbono</h1>
    <p>Este es un espacio para calcular tu huella de carbono.</p>
    <p id="mensaje" style="color:red;"></p>
  </div>

  <!-- Formulario de inicio de sesión -->
  <div id="loginForm" class="hidden">
    <h2>Iniciar sesión</h2>
    <input type="text" id="loginUsuario" placeholder="Nombre de usuario">
    <input type="email" id="loginCorreo" placeholder="Correo electrónico">
    <input type="password" id="loginClave" placeholder="Contraseña">
    <input type="password" id="loginConfirmar" placeholder="Confirmar contraseña">
    <button onclick="iniciarSesion()">Confirmar</button>
    <p>¿Ya tienes cuenta? <button onclick="mostrarRegistro()">Registrate</button></p>
  </div>

  <!-- Formulario de registro -->
  <div id="registroForm" class="hidden">
    <h2>Registrarse</h2>
    <input type="text" id="registroUsuario" placeholder="Usuario o Gmail">
    <input type="password" id="registroClave" placeholder="Contraseña">
    <button onclick="registrarse()">Registrarse</button>
  </div>

  <script>
    let usuario = null;

    function calcular() {
      if (!usuario) {
        document.getElementById("mensaje").textContent = "Hace falta iniciar sesión.";
      } else {
        document.getElementById("mensaje").textContent = "Calculando huella de carbono...";
      }
    }

    function mostrarLogin() {
      document.getElementById("loginForm").classList.remove("hidden");
      document.getElementById("registroForm").classList.add("hidden");
    }

    function mostrarRegistro() {
      document.getElementById("registroForm").classList.remove("hidden");
      document.getElementById("loginForm").classList.add("hidden");
    }

    function iniciarSesion() {
      const usuarioInput = document.getElementById("loginUsuario").value;
      const correo = document.getElementById("loginCorreo").value;
      const clave = document.getElementById("loginClave").value;
      const confirmar = document.getElementById("loginConfirmar").value;

      if (usuarioInput && correo && clave && clave === confirmar) {
        usuario = usuarioInput;
        actualizarUsuario();
        ocultarFormularios();
      } else {
        alert("Completa todos los campos correctamente.");
      }
    }

    function registrarse() {
      const usuarioInput = document.getElementById("registroUsuario").value;
      const clave = document.getElementById("registroClave").value;

      if (usuarioInput && clave) {
        usuario = usuarioInput;
        actualizarUsuario();
        ocultarFormularios();
      } else {
        alert("Completa todos los campos.");
      }
    }

    function actualizarUsuario() {
      const userArea = document.getElementById("userArea");
      userArea.innerHTML = `
        <span>${usuario}</span>
        <button onclick="cerrarSesion()">Cerrar sesión</button>
      `;
    }

    function cerrarSesion() {
      usuario = null;
      document.getElementById("userArea").innerHTML = `<button onclick="mostrarLogin()">Iniciar sesión</button>`;
    }

    function ocultarFormularios() {
      document.getElementById("loginForm").classList.add("hidden");
      document.getElementById("registroForm").classList.add("hidden");
      document.getElementById("mensaje").textContent = "";
    }
  </script>

</body>
</html>
