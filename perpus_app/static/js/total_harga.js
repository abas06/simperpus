document.addEventListener("DOMContentLoaded", function () {
    const jenisTransaksiField = document.getElementById("jenis_transaksi");
    const namaBukuField = document.getElementById("nama_buku");
    const qtyField = document.getElementById("qty");
    const hariField = document.getElementById("hari");
    const hargaField = document.getElementById("harga");

    function calculateTotalHarga() {
        const jenisTransaksi = jenisTransaksiField.value;
        const selectedBuku = namaBukuField.options[namaBukuField.selectedIndex];
        const hargaJual = parseFloat(selectedBuku.getAttribute("data-harga-jual")) || 0;
        const hargaSewa = parseFloat(selectedBuku.getAttribute("data-harga-sewa")) || 0;
        const qty = parseInt(qtyField.value) || 0;
        const hari = parseInt(hariField.value) || 0;

        console.log("Jenis Transaksi:", jenisTransaksi);
        console.log("Harga Jual:", hargaJual, "Harga Sewa:", hargaSewa);
        console.log("Qty:", qty, "Hari:", hari);

        let totalHarga = 0;

        if (jenisTransaksi === "2") { // Beli
            totalHarga = hargaJual * qty;
            hariField.value = "";
            hariField.disabled = true;
        } else if (jenisTransaksi === "1") { // Pinjam
            totalHarga = hargaSewa * qty * hari;
            hariField.disabled = false;
        } else {
            hariField.disabled = false;
        }

        console.log("Total Harga:", totalHarga);
        hargaField.value = totalHarga > 0 ? totalHarga : "";
    }

    jenisTransaksiField.addEventListener("change", calculateTotalHarga);
    [namaBukuField, qtyField, hariField].forEach(field => {
        field.addEventListener("input", calculateTotalHarga);
    });
});