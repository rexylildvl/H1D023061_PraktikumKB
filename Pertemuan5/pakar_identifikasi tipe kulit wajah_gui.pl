% DATABASE JENIS KULIT WAJAH
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA JENIS KULIT
jenis_kulit("Kulit Kering").
jenis_kulit("Kulit Berminyak").
jenis_kulit("Kulit Normal").
jenis_kulit("Kulit Sensitif").
jenis_kulit("Kulit Kombinasi").

% GEJALA UNTUK MASING-MASING KULIT
gejala(kulit_terasa_ketat, "Kulit Kering").
gejala(kulit_bersisik, "Kulit Kering").
gejala(kulit_mudah_teriritasi, "Kulit Sensitif").
gejala(kulit_memerah, "Kulit Sensitif").
gejala(kulit_minyak_di_seluruh_wajah, "Kulit Berminyak").
gejala(pori_pori_besar, "Kulit Berminyak").
gejala(kulit_lunak_dan_kenyal, "Kulit Normal").
gejala(kulit_berminyak_di_T_zone, "Kulit Kombinasi").
gejala(kulit_kering_di_area_pipi, "Kulit Kombinasi").

% PERTANYAAN UNTUK TIAP GEJALA
pertanyaan(kulit_terasa_ketat, "Apakah kulit wajah Anda terasa kencang/kering setelah mencuci muka?").
pertanyaan(kulit_bersisik, "Apakah kulit Anda tampak bersisik atau mengelupas?").
pertanyaan(kulit_mudah_teriritasi, "Apakah kulit Anda mudah mengalami iritasi saat menggunakan produk baru?").
pertanyaan(kulit_memerah, "Apakah kulit Anda sering memerah?").
pertanyaan(kulit_minyak_di_seluruh_wajah, "Apakah wajah Anda tampak berminyak di seluruh area wajah?").
pertanyaan(pori_pori_besar, "Apakah Anda memiliki pori-pori wajah yang besar?").
pertanyaan(kulit_lunak_dan_kenyal, "Apakah kulit Anda terasa lembut dan kenyal tanpa banyak masalah?").
pertanyaan(kulit_berminyak_di_T_zone, "Apakah Anda memiliki minyak berlebih di area T-zone (dahi, hidung, dagu)?").
pertanyaan(kulit_kering_di_area_pipi, "Apakah area pipi Anda terasa kering sementara area lain berminyak?").
