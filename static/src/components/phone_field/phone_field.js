/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PhoneField } from "@web/views/fields/phone/phone_field";
import { SendWAButton } from '@odoo_whatsapp_redirect/components/wa_button/wa_button';

patch(PhoneField, "odoo_whatsapp_redirect.PhoneField", {
    components: {
        ...PhoneField.components,
        SendWAButton
    },
    defaultProps: {
        ...PhoneField.defaultProps,
    },
    props: {
        ...PhoneField.props
    },
    extractProps: ({ attrs }) => {
        return {
            placeholder: attrs.placeholder,
        };
    },
});
