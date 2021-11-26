import os
from pdfrw import PdfWriter, PdfReader, IndirectPdfDict, PdfName, PdfDict, PdfObject


INVOICE_TEMPLATE_PATH = "fp_informe_original.pdf"
INVOICE_OUTPUT_PATH = "resultado.pdf"


ANNOT_KEY = "/Annots"
ANNOT_FIELD_KEY = "/T"
ANNOT_VAL_KEY = "/V"
ANNOT_RECT_KEY = "/Rect"
SUBTYPE_KEY = "/Subtype"
WIDGET_SUBTYPE_KEY = "/Widget"


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):

    template_pdf = PdfReader(input_pdf_path)
    # Para que se vean los campos rellenados
    template_pdf.Root.AcroForm.update(PdfDict(NeedAppearances=PdfObject("true")))
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]

        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():

                        # HACK PARA LOS CHECK - Guardar documento a mano con los checks que sean. Y aquí si es un check, evitarlo y no cambiar
                        if (
                            key == "untitled6"
                            or key == "untitled21"
                            or key == "untitled22"
                            or key == "untitled23"
                            or key == "untitled24"
                            or key == "untitled25"
                        ):

                            continue

                        # this depends on page orientation
                        rct = annotation.Rect
                        hight = round(float(rct[3]) - float(rct[1]), 2)
                        width = round(float(rct[2]) - float(rct[0]), 2)

                        xobj = PdfDict(
                            BBox=[0, 0, width, hight],
                            FormType=1,
                            Resources=PdfDict(ProcSet=[PdfName.PDF, PdfName.Text]),
                            Subtype=PdfName.Form,
                            Type=PdfName.XObject,
                        )
                        # assign a stream to it
                        xobj.stream = (
                            """/Tx BMC
                        BT
                        /Helvetica 8.0 Tf
                        1.0 5.0 Td
                        0 g
                        ("""
                            + data_dict[key]
                            + """) Tj
                        ET EMC"""
                        )
                        annotation.update(
                            PdfDict(AP=PdfDict(N=xobj), V="{}".format(data_dict[key]))
                        )
                        # annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key]),AP='{}'.format(data_dict[key])))

    PdfWriter().write(output_pdf_path, template_pdf)


data_dict = {
    "untitled1": "46025700",  # Codigo de centro
    "untitled5": "Centro",  # Nombre del centro
    "untitled6": PdfName("Yes"),  # Centro titularidad publica
    "untitled2": "Valencia",  # Localidad centro
    "untitled4": "Valencia",  # Provincia centro
    "untitled8": "Numero",  # Telefono Centro
    "untitled3": "Calle Falsa, 123",  # Direccion Centro
    "untitled9": "46900",  # Codigo Postal Centro
    "untitled10": "NIA",  # NIA Alumno
    "untitled11": "Curso",  # Curso Alumno
    "untitled12": "Apellidos, Nombre",  # Apellidos, Nombre - Alumnos
    "untitled15": "Desarrollo de Aplicaciones Web",  # Titulo ciclo
    "untitled16": "Superior",  # Grado ciclo
    "untitled18": "Punto 1.1",  # Punto 1.1
    "untitled17": "Punto 1.2",  # Punto 1.2
    "untitled19": "Punto 1.3",  # Punto 1.3
    "untitled20": "Punto 1.4",  # Punto 1.4
    "untitled21": "true",  # Check Avanzado
    "untitled22": "false",  # Check Intermedio
    "untitled23": "false",  # Check Basico
    "untitled24": "false",  # Check No superado
    "untitled25": "Punto 2.1",  # Punto 2.1
    "untitled26": "Punto 2.2",  # Punto 2.2
    "untitled27": "Punto 2.3",  # Punto 2.3
    "untitled28": "Punto 2.4",  # Punto 2.4
    "untitled30": "Valencia",  # Firma Valencia
    "untitled31": "28",  # Firma dia
    "untitled32": "Mayo",  # Firma Mes
}

# if __name__ == '__main__':
write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)
