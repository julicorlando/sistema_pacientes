<?php
/**
 * Homepage - Index
 * Sistema de Pacientes - PHP Migration
 */

// Set page variables
$page_title = 'Seu Sistema de Pacientes';
$css_files = ['homepage.css'];
$body_class = 'homepage';
$show_nav = true;

// Include common header
require_once 'includes/header.php';

// Get current user if logged in
$user = $auth->getUser();
?>

    <div class="content">
        <h1><strong>Bem-vindo(a)</strong> <?php echo $user ? htmlspecialchars($user['username']) : ''; ?></h1>
        <img src="media/pacientes/Logo/Logo.png" alt="Logo" class="logo">
    </div>
    <div class="content"> 
        <h1>Quem sou eu?</h1>
        <img src="media/pacientes/Logo/Quem.png" alt="Logo" class="">
        
        <h1>Agende uma consulta </h1>
    </div>
    <form id="contactForm">
        <label for="name">Nome:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="phone">Celular:</label><br>
        <input type="tel" id="phone" name="phone" required pattern="\d{11}" placeholder="Digite seu celular (Ex: 81987654321)"><br><br>
        
        <label for="message">Mensagem:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        
        <button type="button" onclick="sendWhatsAppMessage()">Enviar para WhatsApp</button>
    </form>

    <script>
        $(document).ready(function () {
            // Efeito de fade-in na página
            $('body').hide().fadeIn(1000);

            // Efeito de hover para navegação
            $('nav ul li a, .btn').hover(function () {
                $(this).css('background-color', '#d0a0b4');
            }, function () {
                $(this).css('background-color', '');
            });

            // Animação de entrada para o formulário
            $('#contactForm').hide().fadeIn(1500);

            // Função para enviar mensagem pelo WhatsApp
            window.sendWhatsAppMessage = function () {
                const name = $('#name').val();
                const phone = $('#phone').val();
                const message = $('#message').val();
                const phoneNumber = "558192730122";
                const whatsappMessage = `Olá, meu nome é ${name}. Meu número é ${phone}. Mensagem: ${message}`;
                const encodedMessage = encodeURIComponent(whatsappMessage);
                const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
                window.open(whatsappUrl, "_blank");
            };
        });
    </script>

<?php require_once 'includes/footer.php'; ?>