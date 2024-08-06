// static/js/functions.js

// Fungsi untuk memformat angka
function formatHarga(harga) {
    return parseFloat(harga).toLocaleString('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

// Fungsi untuk mengonfirmasi penghapusan
function confirmDelete(event) {
    event.preventDefault(); // Prevent form submission
    var confirmation = confirm("Yakin akan dihapus?");
    if (confirmation) {
        // If user clicks "Yes", submit the form
        event.target.closest('form').submit();
    } else {
        // If user clicks "No", do nothing
        return false;
    }
}

// Seleksi semua elemen dengan class 'harga'
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.harga').forEach(function(element) {
        element.textContent = formatHarga(element.textContent);
    });
});
