import qrcode

def main():
    print('Please enter contact details:')
    first_name   = input(' - Nombres       : ')
    last_name    = input(' - Apellidos        : ')
    email        = input(' - Correo   : ')
    company      = input(' - Compania          : ')
    title        = input(' - Titulo            : ')
    phone_number = input(' - Celular     : ')
    address      = input(' - Direccion          : ')
    okay()
    vcard = make_vcard(first_name, last_name, company, title, phone_number, address, email)
    print(f'Generated vcard:\n{vcard}\n')
    vcf_file = f'{last_name.lower()}.vcf'
    print(f'vCard a escribir: {vcf_file}')
    okay()
    write_vcard(vcard)
    qr(vcard,last_name)


def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        address,
        email):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(vcard):
    return '\n'.join(vcard)

def okay():
    okay = input('Okay [si/no]? ')
    if okay in ['Si', 'si', 'SI', 's', 'S', 'ok']:
        return True
    else:
        print('Cancelado.')
        exit(1)


def qr(vcard, last_name):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    data = '\n'.join(vcard)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f'{last_name.lower()}.png')


if __name__ == "__main__":
    main()