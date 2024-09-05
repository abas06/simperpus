// Fungsi untuk memformat angka
function formatHarga(harga) {
    return parseFloat(harga).toLocaleString('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// Fungsi untuk mengonfirmasi penghapusan
function confirmDelete(event) {
    event.preventDefault(); // Mencegah pengiriman form
    var confirmation = confirm("Yakin akan dihapus?");
    if (confirmation) {
        // Jika user klik "Yes", submit form
        event.target.closest('form').submit();
    } else {
        // Jika user klik "No", tidak melakukan apa-apa
        return false;
    }
}

// Seleksi semua elemen dengan class 'harga' dan format angkanya
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.harga').forEach(function(element) {
        element.textContent = formatHarga(element.textContent);
    });
});