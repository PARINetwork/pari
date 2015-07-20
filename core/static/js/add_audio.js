function addAudio(id) {
    ModalWorkflow({
	url: "/admin/audio/add/?id=" + escape(id)
    });
}
