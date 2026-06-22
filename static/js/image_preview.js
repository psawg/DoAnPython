function previewImage(input, targetId){

    const file = input.files[0];

    if(!file) return;

    const reader = new FileReader();

    reader.onload = function(e){

        document.getElementById(targetId).src =
            e.target.result;

    }

    reader.readAsDataURL(file);
}