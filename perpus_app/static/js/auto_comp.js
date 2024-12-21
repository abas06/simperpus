$(document).ready(function() {
    $("#member_name").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: autocompleteUrl, // Use the dynamically passed URL
                dataType: "json",
                data: {
                    term: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item.nama + " - " + item.no_member,
                            value: item.nama + " - " + item.no_member,
                            id: item.id,
                            no_identitas: item.no_identitas,
                            alamat_ktp: item.alamat_ktp,
                            domisili: item.domisili
                        };
                    }));
                },
                error: function(xhr, status, error) {
                    console.log("Autocomplete error: " + error);
                }
            });
        },
        minLength: 2,
        select: function(event, ui) {
            $("#member_id").val(ui.item.id);
            $("#no_identitas").val(ui.item.no_identitas);
            $("#alamat_ktp").val(ui.item.alamat_ktp);
            $("#domisili").val(ui.item.domisili);
        }
    });
});
