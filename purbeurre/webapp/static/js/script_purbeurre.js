document.addEventListener('DOMContentLoaded', function() {


    if (document.getElementById('account') && document.getElementsByClassName('bg-account')) {

        let btn_img_profil = document.getElementById('profil-image');
        let btn_close_block = document.getElementById('close-form');
        if (btn_img_profil) {
            btn_img_profil.addEventListener('click', modif_profil_img);
            btn_close_block.addEventListener('click', close_box_img);
        };
        
        async function modif_profil_img() {
            let block_img = document.getElementById('modal');
            block_img.setAttribute('style', "");
        };

        async function close_box_img() {
            let block_img = document.getElementById('modal');
            block_img.setAttribute('style', "display: none;");
        };
    };
    
    if (document.getElementById('anim-it')) {
            // Wrap every letter in a span
        let textWrapper = document.querySelector('.ml6 .letters');
        textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
        
        anime.timeline({loop: false})
        .add({
            targets: '.ml6 .letter',
            translateY: ["1.1em", 0],
            translateZ: 0,
            duration: 1000,
            delay: (el, i) => 50 * i
        });
    };

    if (document.getElementsByClassName('reset-confirm-form')) {
        let span = document.querySelector('.helptext');
        let ulbal = document.getElementsByTagName('ul');
        if (ulbal[1]) {
            ulbal[1].remove();
        };
        if (span != null) {
            span.remove();
            form_1 = document.getElementById('id_new_password1');
            form_1.setAttribute('class', 'col-lg-11 form-control  py-1');
            form_2 = document.getElementById('id_new_password2');
            form_2.setAttribute('class', 'col-lg-11 form-control  py-1');
            let labels = document.querySelectorAll('label');
            let label_1 = labels.item(0);
            let label_2 = labels.item(1);
            label_1.setAttribute('class', 'row px-3 text-secondary text-start');
            label_2.setAttribute('class', 'row px-3 text-secondary text-start');
        };
    };


    /********* Alert boxs *********/
    if (document.getElementById('deluser')) {
        

        /********* Begin of alert box delete profil *********/
        let modalContainer = document.createElement('div');
        modalContainer.setAttribute('id', 'modal');
        let customBox = document.createElement('div');
        customBox.className = 'custom-box row col-lg-5 rad-2';
        let btn_d = document.getElementById('deluser');
        btn_d.addEventListener('click', alerte_del_prof);
        
        async function alerte_del_prof(){
            customBox.innerHTML = '<p class="fs-6 text-primary"><strong>Voulez-vous vraiment supprimer votre compte ?</strong></p>';
            customBox.innerHTML += '<p class="fs-6">Cela supprimera également toutes vos données</p>';
            customBox.innerHTML += '<input class="form-control" type="text" id="modal-prompt" placeholder="SUPPRIMER"/><br/>'
            customBox.innerHTML += '<button class="btn my-1 btn-mod" id="modal-close">Annuler</button>';
            customBox.innerHTML += '<button class="text-light btn my-1 bg-red" id="modal-submit">Valider</button>';
            modalShow();
        }

        async function modalShow() {
            modalContainer.appendChild(customBox);
            document.body.appendChild(modalContainer);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose();
            });
            if (document.getElementById('modal-confirm')) {
                document.getElementById('modal-confirm').addEventListener('click', async function () {
                modalClose();
                });
            } else if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    if (document.getElementById('modal-prompt').value == "SUPPRIMER") {
                        window.location.replace("delete_user");
                        modalClose();
                    }
                });
            }
        }

        async function modalClose() {
            while (modalContainer.hasChildNodes()) {
                modalContainer.removeChild(modalContainer.firstChild);
            }
            document.body.removeChild(modalContainer);
        }
        /********* End of alert box delete profil  *********/
        /***************************************************/
        /********* Begin of alert box modif profil *********/
        let modalContainer2 = document.createElement('div');
        modalContainer2.setAttribute('id', 'modal');
        let customBox2 = document.createElement('div');
        customBox2.className = 'custom-box row col-lg-4 rad-2';
        let btn_m = document.getElementById('moduser');
        btn_m.addEventListener('click', modif_profil);
        
        async function modif_profil() {
            customBox2.innerHTML = '<p class="text-primary"><strong>Modifier mon profil</strong></p>';
            customBox2.innerHTML += '<input id="username" autocomplete="off" type="text" name="username" class="form-control" placeholder="Pseudo"/>';
            customBox2.innerHTML += '<input id="first_name" autocomplete="off" type="text" name="first_name" class="form-control" placeholder="Prénom"/>';
            customBox2.innerHTML += '<input id="last_name" autocomplete="off" type="text" name="last_name" class="form-control" placeholder="Nom"/>';
            customBox2.innerHTML += '<input id="password" autocomplete="off" type="text" name="password" class="form-control" placeholder="Mot de passe"/>'
            customBox2.innerHTML += '<button class="btn my-1 btn-mod" id="modal-close">Annuler</button>';
            customBox2.innerHTML += '<button class="text-light btn my-1 bg-green" id="modal-submit">Modifier</button>';
            customBox2.innerHTML += '<p class="text-primary"><strong>Astuce !</br> Cliquez sur votre photo de profil pour la modifier</strong></p>';
            modalShow2();
        }

        async function modalShow2() {
            modalContainer2.appendChild(customBox2);
            document.body.appendChild(modalContainer2);
            document.getElementById('modal-close').addEventListener('click', async function() {
                modalClose2();
            });
            if (document.getElementById('modal-submit')) {
                document.getElementById('modal-submit').addEventListener('click', async function () {
                    let formData = new FormData();
                    formData.append('username', document.getElementById('username').value)
                    formData.append('first_name', document.getElementById('first_name').value)
                    formData.append('last_name', document.getElementById('last_name').value)
                    formData.append('password', document.getElementById('password').value)
                    let request = new Request('modif_user', {method: 'POST', body: formData});
                    fetch(request).then(result => {
                        window.location.replace("account");
                    });
                    modalClose2();
                });
            }
        }

        async function modalClose2() {
            while (modalContainer2.hasChildNodes()) {
                modalContainer2.removeChild(modalContainer2.firstChild);
            }
            document.body.removeChild(modalContainer2);
        }
        /*********  End of alert box modif profil  *********/
    };
    /********* end *********/
});
